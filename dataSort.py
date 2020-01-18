possibleJobs = []
declineJobs = []
coverLetterJobs = []

for key in jobs:
    if 1 in jobs[key][1]:
        possibleJobs.append(key)
    else:
        declineJobs.append(key)
    if 4 not in jobs[key][2]:
        i = possibleJobs.index(key)
        del possibleJobs[i]
        declineJobs.append[key]
    if coverLetter in jobs[key][4]:
        i = possibleJobs.index(k)
        del possibleJobs[i]
        coverLetterJobs.append(key)

#Comment