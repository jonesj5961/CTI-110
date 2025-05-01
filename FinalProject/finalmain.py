# Read in a csv file as a pandas dataframe
import pandas as pd

def manage_df(df):
    # drop unneeded columns
    df = df.drop(columns=['Current Status', 'Status Date', 'Current End Date','Advisor', 'Primary E-Mail', 'Smv Vetben Benefit ', 'Smv Vetben End Date '])
  
    # convert IDs to string
    df['ID'] = df['ID'].apply(lambda x: str(int(float(x))) if pd.notna(x) else '')

    # drop rows where ID or program is blank
    df = df.dropna(subset=['ID'])
    df = df.dropna(subset=['PROGRAMS'])
    
    # find duplicated IDs
    repeated_ids = df['ID'][df['ID'].duplicated(keep=False)]
   
    # filter original DF to only rows with repeated IDs
    df = df[df['ID'].isin(repeated_ids)]

    return df

def associate_combos():
    df = pd.read_csv('Anonymized_SP25_Program_Rosters.csv')
    df = manage_df(df)

    # No more sort_dfs()

    # Create full program descriptions
    df['Program_Desc'] = df['PROGRAMS'] + ' - ' + df['Actual Title']

    # Group programs by student ID
    student_programs = df.groupby('ID')['Program_Desc'].unique().reset_index()
    student_program_codes = df.groupby('ID')['PROGRAMS'].unique().reset_index()

    # Merge descriptions and codes
    student_programs['Program_Codes'] = student_program_codes['PROGRAMS']

    # Define who qualifies: must have at least one Associate and one Certificate or Diploma
    def qualifies(programs):
        has_associate = any(p.startswith('A') for p in programs)
        has_cert_or_diploma = any(p.startswith(('C', 'D')) for p in programs)
        return has_associate and (has_cert_or_diploma or len([p for p in programs if p.startswith('A')]) > 1)

    # Filter to only qualifying students
    qualifying_students = student_programs[student_programs['Program_Codes'].apply(qualifies)]

    # Sort programs alphabetically for consistency
    qualifying_students['Program_Combo'] = qualifying_students['Program_Desc'].apply(
        lambda programs: ', '.join(sorted(programs))
    )

    # Group by program combo and collect IDs
    combo_to_ids = qualifying_students.groupby('Program_Combo')['ID'].apply(list).reset_index()
    combo_to_ids['Count'] = combo_to_ids['ID'].apply(len)
    combo_to_ids = combo_to_ids.sort_values(by='Count', ascending=False)

    print("Most common Associate + Certificate/Diploma combinations (with multiple Associates allowed):")
    
    combo_to_ids.to_csv('program_combinations_with_ids.csv', index=False)

    return combo_to_ids

def cert_dip_combos():
    df = pd.read_csv('Anonymized_SP25_Program_Rosters.csv')
    df = manage_df(df)

    # Identify IDs of students who have any Associate's program
    associate_ids = df[df['PROGRAMS'].str.startswith('A')]['ID'].unique()

    # Remove all records for those IDs
    df = df[~df['ID'].isin(associate_ids)]

    # Create full program descriptions
    df['Program_Desc'] = df['PROGRAMS'] + ' - ' + df['Actual Title']

    # Group remaining programs by student ID
    student_programs = df.groupby('ID')['Program_Desc'].unique().reset_index()
    student_program_codes = df.groupby('ID')['PROGRAMS'].unique().reset_index()

    # Merge descriptions and codes
    student_programs['Program_Codes'] = student_program_codes['PROGRAMS']

    # Define who qualifies: must have at least two non-Associate programs
    def qualifies(programs):
        return len(programs) >= 2 and all(p.startswith(('C', 'D')) for p in programs)

    # Filter to only qualifying students
    qualifying_students = student_programs[student_programs['Program_Codes'].apply(qualifies)]

    # Create sorted combo string
    qualifying_students.loc[:, 'Program_Combo'] = qualifying_students['Program_Desc'].apply(
        lambda programs: ', '.join(sorted(programs))
    )


    # Group by program combo and collect IDs
    combo_to_ids = qualifying_students.groupby('Program_Combo')['ID'].apply(list).reset_index()
    combo_to_ids['Count'] = combo_to_ids['ID'].apply(len)
    combo_to_ids = combo_to_ids.sort_values(by='Count', ascending=False)

    print("Most common Certificate + Certificate/Diploma combinations (excluding Associates):")

    combo_to_ids.to_csv('cert_dip_combinations_with_ids.csv', index=False)
    print(combo_to_ids)

    return combo_to_ids

def main():
    associates_df = associate_combos()
    cert_dip_df = cert_dip_combos()

if __name__ == '__main__':
    main()