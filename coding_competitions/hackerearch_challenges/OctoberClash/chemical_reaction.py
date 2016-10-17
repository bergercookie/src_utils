
T = int(raw_input())
for experiment in xrange(T):
    N = int(raw_input())
    r_names = raw_input().split()
    r_times = [int(i) for i in raw_input().split()]
    r_order = (int(i)-1 for i in raw_input().split())

    names_times = zip(r_names, r_times)
    the_max = 0
    for i in r_order:
        nt = names_times.pop(i)
        if nt[1] > the_max: 
            the_max = nt[1]
        print "{} {}".format(nt[0], the_max)
    print "{} {}".format(names_times[0][0], max(the_max, names_times[0][1]))
