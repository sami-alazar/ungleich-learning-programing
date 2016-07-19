my_name = "me"
hannover_to_basel = 319 
basel_to_hemmiken = 58 
hemmiken_to_gossau = 97 
gossau_to_turbenthal = 34 
turbenthal_to_zollikerberg = 39 
zollikerberg_to_uster= 22 
uster_to_wollishofen= 43 
wollishofen_to_luchsingen= 88 
luchsingen_to_schwanden= 5 
sum = 0

print "Let's talk about %s I just had a long trip."  % my_name 
print "I had to departure from Hannover because that's where I live"

sum = sum + hannover_to_basel
print "It took me around %d from Hannover to Basel" % sum

sum = sum + basel_to_hemmiken
print "It was one of the longst trip in one time because from Basel to Hemmiken took only %d, less than one hour, but %d in total" % (basel_to_hemmiken, sum)
sum = sum + hemmiken_to_gossau
print "Well Hemmiken to Gossau was %d, so far I have traveled %d " % (hemmiken_to_gossau, sum)
sum = sum + gossau_to_turbenthal 
print "I still have long way to drive Gosssau to Turbental %d, and it will be %d." % (gossau_to_turbenthal,sum)
sum = sum + turbenthal_to_zollikerberg
print "We're almost in Zurich just couple of road to hit Turbenthal to Zollikerberg %d and in total %d." % (turbenthal_to_zollikerberg, sum)
sum =sum + zollikerberg_to_uster 
print"The road from Zollikerberg to Uster was clearly piece of cake just %d,  so far I have covered just %d." % (zollikerberg_to_uster, sum)
sum = sum + uster_to_wollishofen    
print "Finally Zurich-Wollishofen long drive %d, in total %d." % (uster_to_wollishofen, sum)
sum = sum + wollishofen_to_luchsingen 
print "Since Zurich is one the close Kantons to Glarus I was able to find a direct highway to Luchsingen but it took me %d more than I expected,it's even more shocking in total %d." % (wollishofen_to_luchsingen, sum) 
sum = sum + luchsingen_to_schwanden 
print " The shortest drive and my final destination Schwanden Known as the Digital City of Glarus was just %d away from luchsingen, in total I traveled %d." %(luchsingen_to_schwanden, sum) 
