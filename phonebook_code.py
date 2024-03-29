from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
import io 



def fix_contacts(contacts_list):
  for item in contacts_list:
    contact_fullname = ' '.join(item[:3]).split()
    return contact_fullname

    
complete = {}
contact_values = [] 
def delete_dup(contacts_list):
    for contact in contacts_list:
      fio = ' '.join(contact[:3]).split()
      contact[:len(fio)] = fio
      names = contact[0]
      if names not in complete:
        complete.update({names: contact})
      else:
        for i, value in enumerate(complete[names]):
          if not value:
            complete[names][i] = contact[i]
    for i, value in complete.items():
      contact_list_updated.append(value)
    return contact_list_updated

        



def fix_phones(contacts_list):
  phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
  phone_substitution = r'+7-(\2) \3-\4-\5'
  
  for phones in contacts_list:
    broken = phones[5]
    if broken == 'phone':
      phones.remove('phone')
    else:
      fixed_phone = re.sub(phone_pattern, phone_substitution, broken).split()
      return fixed_phone




if __name__ == '__main__':
  with io.open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    contact_list_updated = []
    fix_contacts(contacts_list)
    # fix_duplicate(contacts_list)
    fix_phones(contacts_list)
    delete_dup(contacts_list)
  
  with open("phonebook.csv", "w", encoding='utf-8') as out_file:
    datawriter = csv.writer(out_file, delimiter=',')
    datawriter.writerows(contact_list_updated)
  pprint(contact_list_updated)




if __name__ == '__main__':
  with io.open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    contact_list_updated = []
    fix_contacts(contacts_list)
    fix_phones(contacts_list)
    delete_dup(contacts_list)
  
  with open("phonebook.csv", "w", encoding='utf-8') as out_file:
    datawriter = csv.writer(out_file, delimiter=',')
    datawriter.writerows(contact_list_updated)
  pprint(contact_list_updated)
