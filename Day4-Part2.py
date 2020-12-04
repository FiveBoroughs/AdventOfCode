import re


def formatVal(pValue, pValid):
    if(not pValue):
        return '❓'
    if(pValue and not pValid):
        return pValue + '❌'
    return pValue


def normLen(pVal, wsLen):
    return pVal + ' ' * (wsLen - len(pVal) - (1 if pVal.find('❓') != -1 or pVal.find('❌') != -1 else 0))


class User():
    def __init__(self, pbyr, piyr, peyr, phgt, phcl, pecl, ppid, pcid):
        self.byr = pbyr
        self.byrValid = True if pbyr and len(pbyr) == 4 and int(
            pbyr) >= 1920 and int(pbyr) <= 2002 else False

        self.iyr = piyr
        self.iyrValid = True if piyr and len(piyr) == 4 and int(
            piyr) >= 2010 and int(piyr) <= 2020 else False

        self.eyr = peyr
        self.eyrValid = True if peyr and len(peyr) == 4 and int(
            peyr) >= 2020 and int(peyr) <= 2030 else False

        self.hgt = phgt
        self.hgtValid = True if (phgt and (
            True if(phgt.endswith('cm') and int(phgt.rstrip('cm')) >=
                    150 and int(phgt.rstrip('cm')) <= 193) else False
            or
            True if(phgt.endswith('in') and int(phgt.rstrip('in')) >=
                    59 and int(phgt.rstrip('in')) <= 76) else False
        )) else None

        self.hcl = phcl
        self.hclValid = True if phcl and re.compile(
            '^#([a-f0-9]{6})$').match(phcl) else False

        self.ecl = pecl
        self.eclValid = True if pecl and len(
            [x for x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] if x == pecl]) > 0 else False

        self.pid = ppid
        self.pidValid = True if ppid and re.compile(
            '^([0-9]{9})$').match(ppid) else False

        self.cid = pcid

        self.valid = (self.byrValid and
                      self.iyrValid and
                      self.eyrValid and
                      self.hgtValid and
                      self.hclValid and
                      self.eclValid and
                      self.pidValid)

    def __repr__(self):
        return "%s | BYR %s | IYR %s | EYR %s | HGT %s | HCL %s | ECL %s | PID %s | CID %s" % ('✅' if self.valid else '🔴', normLen(formatVal(self.byr, self.byrValid), 6), normLen(formatVal(self.iyr, self.iyrValid), 6), normLen(formatVal(self.eyr, self.eyrValid), 6), normLen(formatVal(self.hgt, self.hgtValid), 7), normLen(formatVal(self.hcl, self.hclValid), 9), normLen(formatVal(self.ecl, self.eclValid), 9), normLen(formatVal(self.pid, self.pidValid), 12), normLen(formatVal(self.cid, True), 3))


with open('Day4-Part1-Input.txt') as f:
    inputs = f.readlines()
rows = list(map(lambda x: x.replace('\n', ''), inputs))

# Parse Users
users = []
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
