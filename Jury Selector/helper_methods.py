import constants
from pandas import DataFrame
# Helper Methods

# Print Methods
def pretty_print(data):
    for category in data:
        print(f"{category}")
        for subcategory in data[category]:
            for value in data[category][subcategory]:
                print(f"\t{subcategory}: {data[category][subcategory][value]}")

def printAll(df):
    for index, row in df.iterrows():
        print(f"Row {index}:")
        for column in df.columns:
            print(f"{column}: {row[column]}")
        print()  # Empty line for separation

def print_jury_ids(chosen_jury):
    index=0
    for juror in chosen_jury:
        print(f"{index+1}: {juror[constants.ID_INDEX]}")
        index+=1


def calculate_breakdown_by_count(jury):
    jury_breakdown = {
    constants.EDUCATION:{
        constants.PRIMARY_EDUCATION:{
            constants.COUNT:0
        },
        constants.UPPER_SECONDARY:{
            constants.COUNT:0
        },
        constants.HIGHER_CERT:{
            constants.COUNT:0
        },
        constants.THIRD_LEVEL_EDUCATION:{
            constants.COUNT:0
        },
    },
    constants.ETHNICITY:{
        constants.WHITE:{
            constants.COUNT:0
        },
        constants.OTHER:{
            constants.COUNT:0
        },
    },
    constants.PROVINCE:{
        constants.LEINSTER:{
            constants.COUNT:0
        },
        constants.MUNSTER:{
            constants.COUNT:0
        },
        constants.CONNACHT:{
            constants.COUNT:0
        },
        constants.ULSTER:{
            constants.COUNT:0
        }
    },
    constants.GENDER:{
        constants.MALE:{
            constants.COUNT:0
        },
        constants.FEMALE:{
            constants.COUNT:0
        },
        constants.OTHER:{
            constants.COUNT:0
        },
    },
    constants.AGE:{
        constants.AGE_18_29:{
            constants.COUNT:0
        },
        constants.AGE_30_44:{
            constants.COUNT:0
        },
        constants.AGE_45_59:{
            constants.COUNT:0
        },
        constants.AGE_60:{
            constants.COUNT:0
        }
    }
}
    
    for juror in jury:
        for category in jury_breakdown:
            sub_cat_index = get_index_from_category(category)
            sub_cat = juror[sub_cat_index]
            jury_breakdown[category][sub_cat][constants.COUNT] = jury_breakdown[category][sub_cat][constants.COUNT] + 1 

    return jury_breakdown


# data cleaning functions
def clean_province_column(province):
    if ',' in province:
        return province.split(', ')[-1]
    return province 

def clean_ethnicity_column(ethnicity):
    if ethnicity == constants.WHITE_IRISH or ethnicity == constants.ANY_OTHER_WHITE:
        return constants.WHITE
    return constants.OTHER

def clean_gender_column(gender):
    if gender != constants.MALE and gender != constants.FEMALE:
        return constants.OTHER
    return gender

def clean_education_column(education):
    if education == constants.PRIMARY_EDUCATION or education == constants.LOWER_SECONDARY:
        return constants.PRIMARY_EDUCATION
    return education

def find_sub_cats_representation(candidate_breakdown, current_jury_breakdown, reverse, thresholds):
    sub_categories = []
    for category in candidate_breakdown:
        for subcategory in candidate_breakdown[category]:
            have =  current_jury_breakdown[category][subcategory][constants.COUNT]
            max = thresholds[category][subcategory][constants.UPPER_THRESHOLD]
            need = thresholds[category][subcategory][constants.LOWER_THRESHOLD]-have
            available = candidate_breakdown[category][subcategory][constants.COUNT]
            if need > 0 and have < max : 
                variance = available-need
                sub_categories.append((category, subcategory, variance))
    return sorted(sub_categories, key=lambda x: x[2], reverse=reverse)

    
def find_most_represented_sub_cat(candidate_breakdown, chosen_jury_breakdown):
    lowest_represented_subcats = find_sub_cats_representation(candidate_breakdown, chosen_jury_breakdown, True)
    for sub_category in lowest_represented_subcats:
        if sub_category[2] != constants.FULLFILLED:
            return sub_category

def count_num_jurors(category, chosen_jury_breakdown):
    sum=0
    for sub_category in chosen_jury_breakdown[category]:
        sum+=chosen_jury_breakdown[category][sub_category][constants.COUNT]
    return sum


def can_add_to_jury(candidate, chosen_jury_breakdown, thresholds):
    for category in chosen_jury_breakdown:
        sub_category = candidate[get_index_from_category(category)]
        current_count_for_sub_category = chosen_jury_breakdown[category][sub_category][constants.COUNT]
        upper_threshold = thresholds[category][sub_category][constants.UPPER_THRESHOLD]
        num_jurors_so_far = count_num_jurors(category, chosen_jury_breakdown)
        if current_count_for_sub_category >= upper_threshold or num_jurors_so_far >= constants.NUM_JURORS:
            return False
    return True

def get_index_from_category(category):
    if category == constants.GENDER:
        return constants.GENDER_INDEX
    elif category == constants.AGE:
        return constants.AGE_INDEX
    elif category == constants.PROVINCE:
        return constants.PROVINCE_INDEX
    elif category == constants.ETHNICITY:
        return constants.ETHNICITY_INDEX
    elif category == constants.EDUCATION:
        return constants.EDUCATION_INDEX

def find_candidate_by_sub_cat(category, sub_category, candidates):
    found = False
    index = 0
    while(not found and index<len(candidates)):
        candidate = candidates[index]
        if candidate[get_index_from_category(category)] == sub_category:
            return candidate
        index+=1
    return None

                
def check_thresholds(breakdown, tresholds):
    for category in breakdown:
        for subcategory in breakdown[category]:
            if breakdown[category][subcategory][constants.COUNT] < tresholds[category][subcategory][constants.LOWER_THRESHOLD]:
                print("Not enough people in: ", category, "->", subcategory)
                return False
    return True

def update_thresholds(breakdown):
    new_thresholds = constants.THRESHOLDS
    for category in new_thresholds:
            for subcategory in new_thresholds[category]:
                count = breakdown[category][subcategory][constants.COUNT]
                old_lower = constants.THRESHOLDS[category][subcategory][constants.LOWER_THRESHOLD]
                old_upper = constants.THRESHOLDS[category][subcategory][constants.UPPER_THRESHOLD]

                new_thresholds[category][subcategory][constants.LOWER_THRESHOLD] = min(old_lower, count)

                if count < old_upper:
                    amount_to_redistribute = old_upper - count
                    new_thresholds[category][subcategory][constants.UPPER_THRESHOLD] = count
                    
                    list_of_sub_cats = []
                    for other_sub_cat in new_thresholds[category]:
                        other_sub_cat_upper = constants.THRESHOLDS[category][other_sub_cat][constants.UPPER_THRESHOLD]
                        list_of_sub_cats.append((other_sub_cat, other_sub_cat_upper))
                    
                    list_of_sub_cats = sorted(list_of_sub_cats, key=lambda x: x[1], reverse=True)
                    biggest_mf = list_of_sub_cats[0]
                    biggest_mf_sub_cat = biggest_mf[0]
                    new_thresholds[category][biggest_mf_sub_cat][constants.UPPER_THRESHOLD] += amount_to_redistribute




                            

    return new_thresholds


def check_sub_category_threshold(category, sub_category, choosen_jury_breakdown, tresholds):
    return choosen_jury_breakdown[category][sub_category][constants.COUNT]>=tresholds[category][sub_category][constants.LOWER_THRESHOLD]
    
def jury_selected(selected_jurors_list, thresholds):
    if len(selected_jurors_list) < constants.NUM_JURORS:
        return False
    else:
        selected_jurors_breakdown = calculate_breakdown_by_count(selected_jurors_list)
        return check_thresholds(selected_jurors_breakdown, thresholds)



def write_to_excel(list_of_juror, name_of_excel):
    ids=[]
    ages=[]
    genders=[]
    provinces=[]
    ethnicities=[]
    educations=[]
    for juror in list_of_juror:
        ids.append(juror[constants.ID_INDEX])
        ages.append(juror[constants.AGE_INDEX])
        genders.append(juror[constants.GENDER_INDEX])
        provinces.append(juror[constants.PROVINCE_INDEX])
        ethnicities.append(juror[constants.ETHNICITY_INDEX])
        educations.append(juror[constants.EDUCATION_INDEX])

    df = DataFrame({constants.ID: ids, constants.AGE: ages, constants.GENDER: genders, constants.PROVINCE: provinces, constants.ETHNICITY: ethnicities, constants.EDUCATION: educations})
    
    df.to_excel(f'{name_of_excel}.xlsx', sheet_name=name_of_excel, index=False)
