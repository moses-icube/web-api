
OTP_NUMBER_OF_DIGITS = 4

# Type of users for Group SMS

ADMINISTRATORS = 1
RECRUITERS = 2
JOBSEEKERS = 3
PROFESSIONAL_USERS = 4

ADMINISTRATORS_LABEL = "Company Administators"
RECRUITERS_LABEL = "Recruiters"
JOBSEEKERS_LABEL = "Jobseekers"
PROFESSIONAL_USER_LABEL = "All Users"

RECIPIENT_CHOICES = (   (ADMINISTRATORS, ADMINISTRATORS_LABEL),
                        (RECRUITERS, RECRUITERS_LABEL),
                        (JOBSEEKERS, JOBSEEKERS_LABEL),
                        (PROFESSIONAL_USERS, PROFESSIONAL_USER_LABEL)
                     )