# Education
EDUCATION = "Education"
PRIMARY_EDUCATION = "No formal/Primary"
LOWER_SECONDARY = "Lower Secondary (Junior/Inter/Group Certificate)"
UPPER_SECONDARY = "Upper Secondary (Leaving certificate)"
HIGHER_CERT = "Higher certificate / apprenticeship / vocational / technical training"
THIRD_LEVEL_EDUCATION = "Graduate degree or higher"

# Ethnicity
ETHNICITY = "Ethnicity"
WHITE_IRISH = "White Irish"
ANY_OTHER_WHITE = "Any other White background"
WHITE = "White"

# Province
PROVINCE = "Province"
LEINSTER = "Leinster"
MUNSTER = "Munster"
CONNACHT = "Connacht"
ULSTER = "Ulster"

# Gender
GENDER = "Gender"
MALE = "Male"
FEMALE = "Female"
OTHER = "Other"

# Age
AGE = "Age"
AGE_18_29 = "18-29 years"
AGE_30_44 = "30-44 years"
AGE_45_59 = "45-59 years"
AGE_60 = "60+ years"

# index
ID_INDEX = 0
GENDER_INDEX = 1
AGE_INDEX = 2
PROVINCE_INDEX = 3
ETHNICITY_INDEX = 4
EDUCATION_INDEX = 5


# 
ID = "ID"
UPPER_THRESHOLD = "Upper Threshold"
LOWER_THRESHOLD = "Lower Threshold"
COUNT = "Count"
PERCENT_FULLFILLED = "Percent Fullfilled"
PERCENT_OVERFLOW = "Percent Overflow"
NUM_JURORS = 25
NUM_SUBS = 25
FULLFILLED = -1
HAVE = "Have"
NEED = "Need"
WANT = "Want"
VARIANCE = "Variance"

# Column Headers
COLUMN_HEADERS={
    ID: "ID",
    AGE: "What age range are you in?",
    GENDER: "Gender",
    PROVINCE: "Province",
    ETHNICITY:"What ethnic group do you most identify with?",
    EDUCATION:"What level of education most closely matches your experience (select the highest level attained)?"
}


THRESHOLDS = {
    EDUCATION:{
        PRIMARY_EDUCATION:{
            LOWER_THRESHOLD: 5,
            UPPER_THRESHOLD: 7,
        },
        UPPER_SECONDARY:{
            LOWER_THRESHOLD: 4,
            UPPER_THRESHOLD: 6,
        },
        HIGHER_CERT:{
            LOWER_THRESHOLD: 4,
            UPPER_THRESHOLD: 6,
        },
        THIRD_LEVEL_EDUCATION:{
            LOWER_THRESHOLD: 8,
            UPPER_THRESHOLD: 10,
        },
    },
    ETHNICITY:{
        WHITE:{
            LOWER_THRESHOLD: 20,
            UPPER_THRESHOLD: 23,
        },
        OTHER:{
            LOWER_THRESHOLD: 3,
            UPPER_THRESHOLD: 5,
        },
    },
    PROVINCE:{
        LEINSTER:{
            LOWER_THRESHOLD: 11,
            UPPER_THRESHOLD: 13,
        },
        MUNSTER:{
            LOWER_THRESHOLD: 6,
            UPPER_THRESHOLD: 8,
        },
        CONNACHT:{
            LOWER_THRESHOLD: 2,
            UPPER_THRESHOLD: 4,
        },
        ULSTER:{
            LOWER_THRESHOLD: 1,
            UPPER_THRESHOLD: 3,
        }
    },
    GENDER:{
        MALE:{
            LOWER_THRESHOLD: 11,
            UPPER_THRESHOLD: 13,
        },
        FEMALE:{          
            LOWER_THRESHOLD: 11,
            UPPER_THRESHOLD: 13,
        },
        OTHER:{           
            LOWER_THRESHOLD: 0,
            UPPER_THRESHOLD: 2,
        },
    },
    AGE:{
        AGE_18_29:{           
            LOWER_THRESHOLD: 4,
            UPPER_THRESHOLD: 6,
        },
        AGE_30_44:{         
            LOWER_THRESHOLD: 6,
            UPPER_THRESHOLD: 8,
        },
        AGE_45_59:{           
            LOWER_THRESHOLD: 6,
            UPPER_THRESHOLD: 8,
        },
        AGE_60:{           
            LOWER_THRESHOLD: 6,
            UPPER_THRESHOLD: 8,
        }
    }
}
