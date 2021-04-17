import random, csv, uuid, lorem

# Variables
companies = ['Spotify', 'Klarna', 'King', 'Mojang', 'Unibet', 'Google', 'Facebook', 'Apple', 'Netflix', 'iZettle']
#fompanies = ['Scotty-Phi', 'Kvarna', 'Queen', 'Mogang', 'DuoBet', 'Foogle', 'BaseBook', 'Pear', 'WebFlicks', 'uPay'] #Fake companies

job_titles = ['Front-End Developer', 'Back-End Developer', 'Mobile Developer', 'QA Developer', 'DevOps Engineer', 'Cloud Engineer', 'HR Officer', 'UX Designer']
seniorities_matrix = [['Intern', 1], ['Junior', 3], ['Mid-level', 6], ['Senior', 4], ['Lead', 2], ['Principal', 1]]
# Different levels of seniorities + their weight as a probability
seniorities = [row[0] for row in seniorities_matrix]
seniorities_weights = [row[1] for row in seniorities_matrix]  

countryCodes = ['se', 'uk', 'us', 'de', 'da', 'no', 'fi', 'fr', 'it', 'ca', 'es', 'ru', 'cn', 'jp', 'in']

fnames = ['company', 'reviewId', 'reviewEditCode', 'jobDescription', 'reviewBody', 'reaction1', 'reaction2', 'reaction3', 'reaction4', 'country']

def getFakeReview():
  return {
          fnames[0] : random.choice(companies), 
          fnames[1] : str(uuid.uuid4())[:8],
          fnames[2] : str(uuid.uuid4())[:8],
          fnames[3] : random.choices(seniorities, weights=seniorities_weights, k=1)[0] + ' ' + random.choice(job_titles),
          fnames[4] : lorem.get_paragraph(count=random.randint(1,3)),
          fnames[5] : max(int(random.gauss(1, 7)), 0),
          fnames[6] : max(int(random.gauss(1, 3)), 0),
          fnames[7] : max(int(random.gauss(1, 2)), 0),
          fnames[8] : max(int(random.gauss(1, 1)), 0),
          fnames[9] : random.choices(countryCodes)[0],
          }



with open('data.csv', 'w') as f:
  csv.register_dialect('semicolon', delimiter=';')
  writer = csv.DictWriter(f, fieldnames=fnames, dialect='semicolon')
  writer.writeheader()
  for i in range(1000):
    writer.writerow(getFakeReview())