class Job(object):
    def __init__(self, s, f):
        self.s = s
        self.f = f

    def __str__(self):
        return ("start: {} finish: {}".format(self.s, self.f))

def max_jobs(jobs):
    S = [jobs[0]]
    del jobs[0]
    while jobs:
        if jobs[0].s >= S[-1].f:
            S.append(jobs[0])
            del jobs[0]
        else:
            del jobs[0]
    return S

def test_1():
    lst = [Job(0, 6), Job(1,4), Job(3,5), Job(3, 8), Job(4, 7), Job(5,9),
            Job(6, 10), Job(8, 11)]
    lst.sort(key = lambda x: x.f)
    return lst

def main():
    jobs = max_jobs(test_1())
    assert(jobs[0].s == 1)
    assert(jobs[0].f == 4)
    assert(jobs[1].s == 4)
    assert(jobs[1].f == 7)
    assert(jobs[2].s == 8)
    assert(jobs[2].f == 11)

if __name__ == '__main__':
    main()
