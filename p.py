import pandas as pd

time_plan = [("Phase I: Introduction and Background Research", "4 weeks", "- Review existing literature and studies on the topic\n\nDefine research questions and objectives\nDevelop an outline for the thesis\nConduct initial research", "10th Feb."),
("Phase II: Data Collection and Analysis", "8 weeks", "- Develop and implement data collection methods\n\nAnalyze collected data\nConduct additional research as needed\nStart writing up the results of the data analysis", "8th Mar."),
("Phase III: Results and Discussion", "5 weeks", "- Write up the results of the data analysis in detail\n\nDiscuss the results and their implications\nDevelop conclusions and recommendations", "5th Apr."),
("Phase IV: Finalizing the Thesis", "4 weeks", "- Revise and edit the entire thesis\n\nPrepare the final draft\nGet feedback from supervisor and peers\nMake final revisions and improvements", "3rd May."),
("Phase V: Final Submission and Presentation", "2 weeks", "- Submit the final draft of the thesis\n\nPrepare for the final presentation\nMake any final revisions based on feedback received during the presentation", "17th May.")]

df = pd.DataFrame(time_plan, columns=['Phase', 'Time Span', 'Tasks', 'Starting Date'])

df.to_csv('time_plan.csv', index=False)

phase_I = df.iloc[0].to_list()
phase_II = df.iloc[1].to_list()
phase_III = df.iloc[2].to_list()
phase_IV = df.iloc[3].to_list()
phase_V = df.iloc[4].to_list()