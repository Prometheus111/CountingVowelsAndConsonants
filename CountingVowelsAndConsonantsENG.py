# CountingVowelsAndConsonantsENG.py
# by Prometheus111

#counting vowels and consonants in the entered text

#request to enter and translate the entered letters into lowercase
i = input('Enter the text: \n').lower()
#vowels & consonants for ENG
g = ['a','e','i','o','u','y']
s = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
#output the results
print('Number of vowels: ', len([1 for x in list(i) if x in g]))
print('Number of consonants: ', len([1 for x in list(i) if x in s]))
Enjoy learning new things! Prometheus111 helps you with your studying!
# https://github.com/Prometheus111 
