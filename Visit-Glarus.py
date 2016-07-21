zurich_to_glarus = 69 
chur_to_glarus = 65
geneva_to_glarus = 260	
Bern_to_glarus = 160
winterthur_to_glarus = 100
aarau_to_glarus = 115
zug_to_glarus = 107
luzern_to_glarus = 131
bellizona_to_glarus = 210
schaffhausen_to_glarus = 140
olten_to_glarus = 111
kantons = 11
sumall = chur_to_glarus + geneva_to_glarus + Bern_to_glarus + winterthur_to_glarus + aarau_to_glarus + zug_to_glarus + luzern_to_glarus + bellizona_to_glarus + schaffhausen_to_glarus + olten_to_glarus 


print "Visit Kanton Glarus from where ever you are."
print  "Zurich to Glarus %d min." % zurich_to_glarus
print  "Chur to Glarus %d min." % chur_to_glarus
print  "Geneva to Glarus %d min." % geneva_to_glarus
print  "Bern to Glarus %d min." % Bern_to_glarus
print  "Winterthur to Glarus %d min." % winterthur_to_glarus
print  "Aarau to Glarus %d min." % aarau_to_glarus
print  "Zug to Glarus %d min." % zug_to_glarus
print  "Luzern to Glarus %d min." % luzern_to_glarus
print  "Bellizona to Glarus %d min." % bellizona_to_glarus
print  "Schaffhausen to Glarus %d min." % schaffhausen_to_glarus 
print  "Olten to Glarus %d min." % olten_to_glarus 

print sumall
average = sumall / kantons
print "Average time that you cant travel is " ,average, "min ."

print "So please you are very welcome to visit our beautiful mountains!!!!"
