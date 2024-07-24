import pandas as pd
import os
import sys
from helper_methods import clean_ethnicity_column, update_thresholds, jury_selected, check_sub_category_threshold, check_thresholds, find_sub_cats_representation, can_add_to_jury, pretty_print, find_candidate_by_sub_cat, clean_education_column, clean_gender_column, clean_province_column, calculate_breakdown_by_count
import constants

file_path = 'Data\FINAL Data Set 2024 - Copy.xlsx'

if not os.path.exists(file_path):
    print(f"The file at path {file_path} does not exist.")
    sys.exit()
else:
    try:
        df = pd.read_excel(file_path)
    except PermissionError as e:
        print(f"PermissionError: {e}")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()


try:
    df=df.rename(columns = {constants.COLUMN_HEADERS.get(constants.AGE):constants.AGE})
    df=df.rename(columns = {constants.COLUMN_HEADERS.get(constants.GENDER):constants.GENDER})
    df=df.rename(columns = {constants.COLUMN_HEADERS.get(constants.PROVINCE):constants.PROVINCE})
    df=df.rename(columns = {constants.COLUMN_HEADERS.get(constants.ETHNICITY):constants.ETHNICITY})
    df=df.rename(columns = {constants.COLUMN_HEADERS.get(constants.EDUCATION):constants.EDUCATION})

    # Applying Data cleansing functions
    df[constants.PROVINCE] = df[constants.PROVINCE].apply(clean_province_column)
    df[constants.ETHNICITY] = df[constants.ETHNICITY].apply(clean_ethnicity_column)
    df[constants.GENDER] = df[constants.GENDER].apply(clean_gender_column)
    df[constants.EDUCATION] = df[constants.EDUCATION].apply(clean_education_column)
except Exception as e:
    print(f"Error occured during data cleansing: {e}")


# Add a variable for each person, where the value is either 0 (not selected) or 1 (selected)
candidates = []
for _, row in df.iterrows():
    variable = (row[constants.ID], row[constants.GENDER], row[constants.AGE], row[constants.PROVINCE], row[constants.ETHNICITY], row[constants.EDUCATION])
    candidates.append(variable)


chosen_jury = []
not_selected = []
chosen_jury_breakdown = calculate_breakdown_by_count(chosen_jury)
candidate_breakdown = calculate_breakdown_by_count(candidates)

unsatisfied_categories = find_sub_cats_representation(candidate_breakdown, chosen_jury_breakdown, False, constants.THRESHOLDS)

while not jury_selected(chosen_jury):
    if len(unsatisfied_categories) > 0:
        unsatisfied_category_info = unsatisfied_categories[0]
        unsatisfied_category = unsatisfied_category_info[0]
        unsatisfied_sub_category = unsatisfied_category_info[1]

        while not check_sub_category_threshold(unsatisfied_category, unsatisfied_sub_category, chosen_jury_breakdown):
            potential_candidate = find_candidate_by_sub_cat(unsatisfied_category, unsatisfied_sub_category, candidates)
            if can_add_to_jury(potential_candidate, chosen_jury_breakdown):
                chosen_jury.append(potential_candidate)
            else:
                most_represented_sub_cat_info = unsatisfied_categories[-1]
                most_represented_cat = most_represented_sub_cat_info[0]
                most_represented_sub_cat = most_represented_sub_cat_info[1]
                candidate_to_remove = find_candidate_by_sub_cat(most_represented_cat, most_represented_sub_cat, chosen_jury)
                chosen_jury.remove(candidate_to_remove)
                candidates.append(candidate_to_remove)
                not_selected.append(potential_candidate)
                chosen_jury_breakdown = calculate_breakdown_by_count(chosen_jury)
                candidate_breakdown = calculate_breakdown_by_count(candidates)
                unsatisfied_categories = find_sub_cats_representation(candidate_breakdown, chosen_jury_breakdown, False, constants.THRESHOLDS)
            
            if potential_candidate in candidates: 
                candidates.remove(potential_candidate)
                

            chosen_jury_breakdown = calculate_breakdown_by_count(chosen_jury)
            candidate_breakdown = calculate_breakdown_by_count(candidates)
        
        unsatisfied_categories = [tup for tup in unsatisfied_categories if tup[1] != unsatisfied_sub_category]

    else:
        candidate_to_add = candidates[0]
        if can_add_to_jury(candidate_to_add, chosen_jury_breakdown):
            chosen_jury.append(candidate_to_add)
        else:
            not_selected.append(candidate_to_add)

        candidates.remove(candidate_to_add)

        chosen_jury_breakdown = calculate_breakdown_by_count(chosen_jury)
        candidate_breakdown = calculate_breakdown_by_count(candidates)
            

    
#pretty_print(chosen_jury_breakdown)
if check_thresholds(chosen_jury_breakdown):
    print("Jury Found moving to subs")
# print(len(chosen_jury))
# write_to_excel(chosen_jury)





print("Remaining Candidates to get subs:")



chosen_subs = []
chosen_subs_breakdown = calculate_breakdown_by_count(chosen_subs)
candidates.extend(not_selected)
remaining_candidates_breakdown = calculate_breakdown_by_count(candidates)

sub_thresholds = constants.THRESHOLDS
if not check_thresholds(remaining_candidates_breakdown):
    sub_thresholds = update_thresholds(remaining_candidates_breakdown)


unsatisfied_categories = find_sub_cats_representation(remaining_candidates_breakdown, chosen_subs_breakdown, False, sub_thresholds)

print(unsatisfied_categories)









