possibleJobs = [] # Jobs that don't require a cover letter
declineJobs = [] # Jobs not meeting the qualifications
coverLetterJobs = [] # Jobs requiring a cover letter that meet qualifications

for key in jobs:
    # Checks work level
    if 1 in jobs[key][1]:
        possibleJobs.append(key)
    else:
        declineJobs.append(key)
    # Checks work duration
    if 4 not in jobs[key][2]:
        i = possibleJobs.index(key)
        del possibleJobs[i]
        declineJobs.append[key]
    # Checks cover letter requirement
    if coverLetter in jobs[key][4]:
        i = possibleJobs.index(k)
        del possibleJobs[i]
        coverLetterJobs.append(key)

