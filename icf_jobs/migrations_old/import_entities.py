import csv
import os, sys
import random
import shutil

import PIL
from allauth.account import signals
from pip._vendor.distlib.compat import raw_input



FILE_DIR=os.path.dirname(os.path.abspath(__file__))
PROJ_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "icf.settings")
sys.path.append(PROJ_PATH)

# This is so my local_settings.py gets loaded.
os.chdir(PROJ_PATH)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from icf_auth.models import User
from icf_jobs.migrations_old.Utility import Utility
from icf_entity.models import Sector, Entity, CompanySize, Logo, EntityUser
from icf_generic.models import Address, City
import datetime
from django.db import transaction
from icf_auth.migrate_old_system.Helper import Helper
import PIL.Image
from django.core.files import File
import logging

logger = logging.getLogger(__name__)


# cur = con.cursor()

# ENTITY_FILE = os.path.join(FILE_DIR, "companies-temp-data.csv")
ENTITY_FILE = os.path.join(FILE_DIR, "companies-with-names-2.csv")
WRITE_ENTITY_SAVED_FILE = os.path.join(FILE_DIR, "companies-save-success.csv")
WRITE_ENTITY_UNSAVED_FILE = os.path.join(FILE_DIR, "companies-save-failed.csv")
WRITE_NOT_FOUND_FOR_ENTITY_FILE = os.path.join(FILE_DIR, "user_not_found_for_entity.py")

ENTITY_IMAGE_PATH= os.path.join(FILE_DIR, "companyLogos")
IMAGE_MAX_HEIGHT = IMAGE_MAX_WIDTH = 200
# USERS_RESUME_FILE = os.path.join(FILE_DIR, "users-resume-temp-data.csv")


def create_thumbnail(orig_image_path, max_height=200, max_width=200):

    # print("Create a new thumbnail for {0}".format(orig_image_path))
    logger.info("Create a new thumbnail for {0}".format(orig_image_path))

    orig_filename = os.path.basename(orig_image_path)

    try:
        orig_image = PIL.Image.open(orig_image_path)
    except ValueError:
        # print("Could not open the file at {0}".format(orig_image_path))
        logger.info("Could not open the file at {0}".format(orig_image_path))
        raise
    except Exception as e:
        raise

    orig_file_basename, ext = os.path.splitext(orig_filename)

    size = (max_height, max_width)

    orig_image.thumbnail(size, PIL.Image.ANTIALIAS)

    tmp_dir = "%s/tmp" % FILE_DIR
    if not os.path.exists(tmp_dir):
        try:
            os.makedirs(tmp_dir)
        except OSError as ose:
            # print("Cannot create directory {0}, error {1}".format(tmp_dir, ose.strerror))
            logger.info("Cannot create directory {0}, error {1}".format(tmp_dir, ose.strerror))
            raise


    #
    # If the filename already exists in the tmp directory, create the file in another temp directory
    #
    tmp_file_path = os.path.join(tmp_dir, orig_filename)
    if os.path.exists(tmp_file_path):
        temp_path = os.path.join(tmp_dir, "%s" % random.random)
        try:
            os.makedirs(temp_path)
            tmp_file_path = os.path.join(temp_path, orig_filename)
        except OSError as ose:
            # print("Cannot create directory, error {0}".format(ose.strerror))
            logger.info("Cannot create directory, error {0}".format(ose.strerror))
            raise

    try:
        orig_image = orig_image.convert('RGB')
        orig_image.save(tmp_file_path)
    except KeyError:
        logger.info("Ambiguous format, not a valid image filename")
        raise
    except IOError:
        logger.info("IO Error, Could not write to file")
        raise

    thumb_data = open(tmp_file_path, "rb")

    thumb_file = File(thumb_data)

    return thumb_file


with open(ENTITY_FILE, "rt", encoding="utf8") as fin: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    try:
        entity_save_success_file = open(WRITE_ENTITY_SAVED_FILE, "a+")
        entity_save_failure_file = open(WRITE_ENTITY_UNSAVED_FILE, "a+")
        user_not_found_for_entity_file = open(WRITE_NOT_FOUND_FOR_ENTITY_FILE, "a+")



        entity_image_logo_path = raw_input("enter directory paths of image files:\n")
        entity_image_logo_path = entity_image_logo_path.lstrip().rstrip()
        if not entity_image_logo_path.lstrip().rstrip():
            raise ValueError("Please enter user imagefile path")
        if not (os.path.isdir(entity_image_logo_path.lstrip().rstrip())):
            raise ValueError("Please enter proper directory path ")

        for row in dr:
            if row['company_state'] == '1':
                company_id = row['company_id']
                email_id = row['email_id'].lstrip().rstrip()
                name = row['name'].lstrip().rstrip()
                registration_date = row['registration_date'].lstrip().rstrip()
                company_state = row['company_state'].lstrip().rstrip()
                logo_url=row['logo_url'].lstrip().rstrip()
                telephone_code = row['telephone_code'].lstrip().rstrip()
                telephone_no = row['telephone_no'].lstrip().rstrip()
                web_adr = row['web_adr'].lstrip().rstrip()
                alternate_tele_no = row['alternate_tele_no'].lstrip().rstrip()

                phone = "+{telephone_code}{telephone_no}".format(telephone_code=telephone_code, telephone_no=telephone_no)
                alternate_phone = "+{telephone_code}{alternate_tele_no}".format(telephone_code=telephone_code, alternate_tele_no=alternate_tele_no)

                registered_address_city = row['registered_address_city'].lstrip().rstrip()

                registered_address_1 = row['registered_address_1'].lstrip().rstrip()
                registered_address_2 = row['registered_address_2'].lstrip().rstrip()
                company_admin = row['company_admin'].lstrip().rstrip() ##   company_admin email field to be searched in Users Table
                sectorname  = row['sectorname'].lstrip().rstrip()
                industryname = row['industryname'].lstrip().rstrip()
                companysize = row['companysize'].lstrip().rstrip()


                try:

                    # type_name = 'entity'
                    # type = Utility.get_type(type_name)
                    with transaction.atomic():

                            city = Utility.get_city(registered_address_city)

                            address = Address.objects.create(address_1=registered_address_1, address_2=registered_address_2, city=city)

                            # try:
                            #     company_size = CompanySize.objects.get(size=companysize)

                            company_size = Utility.get_company_size(companysize)

                            if sectorname:
                                # sector = Utility.get_sector(sectorname)
                                sector = None

                            if industryname:
                                industry = Utility.get_industry(industryname)
                                category = Utility.get_category(industryname)

                            entity = Entity.objects.create(name=name, email=email_id, phone=phone, alternate_phone=alternate_phone,
                                                           website=web_adr, description='', status=company_state, address=address,
                                                           company_size=company_size, industry=industry, sector=sector, category=category)

                            if company_admin:
                                try:
                                    user = User.objects.get(email=company_admin)
                                    entity_user = EntityUser.objects.create(entity=entity,user=user)
                                except User.DoesNotExist as e:
                                    user_not_found_for_entity_file.write("{email}\n".format(email=company_admin))
                                    raise      #### this line of code should be changed

                            if logo_url:
                                logo = Logo()
                                logo.entity = entity
                                try:

                                    # img_data = create_thumbnail(os.path.join(USER_IMAGE_PATH, profile_image_url), IMAGE_MAX_HEIGHT, IMAGE_MAX_WIDTH)
                                    image_full_path = os.path.join(str(entity_image_logo_path), logo_url)
                                    if os.path.exists(image_full_path):
                                        img_data = create_thumbnail(image_full_path, IMAGE_MAX_HEIGHT,
                                                                    IMAGE_MAX_WIDTH)
                                        img_file = File(img_data)
                                        logo.image.save(logo_url, img_file)
                                        logo.save()

                                # except FileNotFoundError as fne:
                                #     pass

                                # except User.DoesNotExist as ude:
                                #     raise
                                except IOError as e:
                                    logger.info("No Such file or directory  - {}".format(e))
                                    raise
                            entity_save_success_file.write("{row}\n".format(row=row))
                            logger.info("create entity successful with - {row}".format(row=row))
                except Exception as e:
                    # entity_save_failure_file.write("{entity}\n".format(entity=entity.name))
                    entity_save_failure_file.write("{row}\n".format(row=row))
                    logger.info(
                        "Could not create entity  with - {row},{exception}".format(row=row, exception=e))
    finally:
        entity_save_success_file.close()
        entity_save_failure_file.close()