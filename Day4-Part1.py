import math

with open('Day4-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

users = []


def prNn(pVal):
    return pVal if pVal else '❓'


def normLen(pVal, wsLen):
    return pVal + ' ' * (wsLen - len(pVal) - (1 if pVal == '❓' else 0))


class User():
    def __init__(self, pbyr, piyr, peyr, phgt, phcl, pecl, ppid, pcid):
        self.byr = pbyr
        self.iyr = piyr
        self.eyr = peyr
        self.hgt = phgt
        self.hcl = phcl
        self.ecl = pecl
        self.pid = ppid
        self.cid = pcid
        self.valid = (self.byr != None and
                      self.iyr != None and
                      self.eyr != None and
                      self.hgt != None and
                      self.hcl != None and
                      self.ecl != None and
                      self.pid != None)

    def __repr__(self):
        return "%s | BYR %s | IYR %s | EYR %s | HGT %s | HCL %s | ECL %s | PID %s | CID %s" % ('✅' if self.valid else '🔴', normLen(prNn(self.byr), 4), normLen(prNn(self.iyr), 4), normLen(prNn(self.eyr), 4), normLen(prNn(self.hgt), 5), normLen(prNn(self.hcl), 7), normLen(prNn(self.ecl), 7), normLen(prNn(self.pid), 10), normLen(prNn(self.cid), 3))


# Parse Users
draftUserRows = []
for row in rows:
    # print('row', row)
    if row != '':
        draftUserRows.append(row)
    else:
        # New User
        # print('draft user', draftUserRows)
        draftUserRowParts = []
        for draftUserRow in draftUserRows:
            for part in draftUserRow.split(' '):
                draftUserRowParts.append(part)
        # print('parts', draftUserRowParts)
        byr = [
            part.split(':')[1] for part in draftUserRowParts if part.startswith('byr:')]
        iyr = [
            part.split(':')[1] for part in draftUserRowParts if part.startswith('iyr:')]
        eyr = [
            part.split(':')[1] for part in draftUserRowParts if part.startswith('eyr:')]
        hgt = [
            part.split(':')[1] for part in draftUserRowParts if part.startswith('hgt:')]
        hcl = [
            part.split(':')[1] for part in draftUserRowParts if part.startswith('hcl:')]
        ecl = [
            part.split(':')[1] for part in draftUserRowParts if part.startswith('ecl:')]
        pid = [
            part.split(':')[1] for part in draftUserRowParts if part.startswith('pid:')]
        cid = [
            part.split(':')[1] for part in draftUserRowParts if part.startswith('cid:')]
        user = User((byr[:1] or [None])[0],
                    (iyr[:1] or [None])[0],
                    (eyr[:1] or [None])[0],
                    (hgt[:1] or [None])[0],
                    (hcl[:1] or [None])[0],
                    (ecl[:1] or [None])[0],
                    (pid[:1] or [None])[0],
                    (cid[:1] or [None])[0])

        users.append(user)
        draftUserRows.clear()

# Check passport validity
validUserCount = 0
for user in users:
    if (user.valid):
        validUserCount += 1
    # else:
    print(user)
print(len(users), 'users')
print(validUserCount, 'valid users')
