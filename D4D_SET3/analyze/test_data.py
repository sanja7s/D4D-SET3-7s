'''
Created on Jan 4, 2013

@author: sscepano
'''

from collections import defaultdict, OrderedDict

def print_data_stats(data):
    
#    print ("Number of users found in data: " , len(data))
    
#    i = 0
#    count_users_no_calls_at_night = 0
#    
#    max_subprefs = 0
#    max_usr = 0
#    
#    for usr in data.iterkeys():
#        i = i + 1
##        print ("Subprefs per user: ", usr, " ", data[usr])
##        if i == 100:
##            break
#        if data[usr] == 0:
#            count_users_no_calls_at_night += 1
#            #print ("Users without calls at night: ", usr, data[usr])
#        else:
#            if len(data[usr]) > max_subprefs:
#                max_subprefs = len(data[usr])
#                max_usr = usr
#    
#    print ("Users without calls at night: ", count_users_no_calls_at_night)
#    print("User with most visited subprefs: ", max_usr, max_subprefs)
#    print("Testing previous statement: ", data[max_usr], len(data[max_usr]))
#    
#    print("Testing previous statement: ", data['1'])
#    print("Testing previous statement: ", data['0'])
#    print("Testing previous statement: ", data['10'])
#    print("Testing previous statement: 458429", data['458429'])
#    print("Testing previous statement: 179359", data['179359'])
#    print("Testing previous statement: 232647", data['232647'])
#    print("Testing previous statement: 86183", data['86183'])
#    print("Testing previous statement: 154401", data['154401'])
#    print("Testing previous statement: 423160", data['423160'])
    
#    print("Testing previous statement: 77777", data['77777'])
        
        
#    home = defaultdict(int)
#    home_simple = defaultdict(int)
#    
#    testi = 0
#
#    for usr in data.iterkeys():
#        if data[usr] <> 0:
#            testi += 1
#            home[usr] = OrderedDict(sorted(data[usr].items(), key=lambda t: t[1], reverse=True)) 
##            if testi < 100:
##                print home[usr].popitem(last=False)[0]
#            
#    fileout = 'Users_and_their_homes.tsv'
#    f = open(fileout, 'w')
#    
#    for usr in home.iterkeys():
#        try:
#            #f.write(usr + '\t' + home[usr].popitem(last=False)[0] + '\n')
#            home_simple[usr] = home[usr].popitem(last=False)[0]
#        except KeyError:
#            print(usr)
#            
#    f.close()
#         
#    subpref_home = defaultdict(int)    
#    for usr in home_simple.iterkeys():
#        try:
#            subpref_home[home_simple[usr]].append(usr)
#        except AttributeError:
#            subpref_home[home_simple[usr]] = [usr]
#    
#    testi = 0
#    for subpref in subpref_home.iterkeys():
#        print subpref_home[subpref]
#        testi += 1
#        if testi > 1:
#            break
#        
#    fileout2 = 'Subprefs_and_their_users.tsv'
#    f2 = open(fileout2, 'w')
#    
#    count_users_check = 0
#    
#    for subpref in subpref_home.iterkeys():
#        f2.write(subpref + ':')
#        for usr in subpref_home[subpref]:
#            f2.write('\t' + usr)
#            count_users_check += 1
#        f2.write('\n')
#        
#    f2.close()   
#    print count_users_check
#    print len(subpref_home)
#    
#    for i in range (256):
#        if str(i) not in subpref_home.iterkeys():
#            print i
    
    
    file_name1 = "Users_and_their_homes.tsv"
    file_name2 = "Users_and_their_homes_total.tsv"
    
    f1 = open(file_name1, 'r')
    f2 = open(file_name2, 'r')
    
    usr_home = defaultdict(int)
    count = 0
    
    for line1 in f1:
        usr, home = line1.split('\t')
        count += 1
#        print usr
#        print home
        usr = int(usr)
        home = int(home[:-1])
        usr_home[usr] = home
#        if count > 100:
#            break

    print count
        
#    for i in range (2550):
#        print (i, usr_home[i])
        
    count_diff = 0
    count_same = 0
    count_all = 0
    
    for line2 in f2:
        count_all += 1
        usr, home = line2.split('\t')
        usr = int(usr)
        home = int(home)
        if usr_home[usr] <> home:
            count_diff += 1
            #if count_diff < 22000 and count_diff > 21900:
                #print ('Usr ',usr, 'Old home ', usr_home[usr], 'New home ', home )
        if usr_home[usr] == home:
            count_same += 1
            
    print count_diff
    print count_same
    print count_all
    
    return


#def sum_data(dataA, dataB, dataC, dataD, dataE, dataF, dataG, dataH, dataI, dataJ):
#    
#    data = defaultdict(int)
#    for usr in dataA.iterkeys():
#        for subpref in dataA[usr].iterkeys():
#            data[usr][subpref] = dataA[usr][subpref] + dataB[usr][subpref] + dataC[usr][subpref] + dataD[usr][subpref] + dataE[usr][subpref] + dataF[usr][subpref] + dataG[usr][subpref] + dataH[usr][subpref] + dataI[usr][subpref] + dataJ[usr][subpref]
#    
#    return data