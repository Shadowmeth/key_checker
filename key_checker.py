def key_check(mega_relation, fds, candidate_keys):
    closure = []
    for attribute in candidate_keys:
        closure.append(attribute)

    for attribute in candidate_keys:
        try:
            left = fds[attribute]
            for attributes in left:
                closure.append(attributes)
        except:
            continue

    for attribute in closure:
        try:
            left = fds[attribute]
            for attributes in left:
                if attributes not in closure:
                    closure.append(attributes)
        except:
            continue
    return len(mega_relation) == len(closure)


mega_relation = input("Enter mega relation (space seprated): ")
mega_relation = mega_relation.split()

A = {}
fds = input("Enter list of FDs seprated by space (-1 to end): ")
while fds != "-1":
    fds = fds.split()
    for i in range(1, len(fds)):
        A[fds[0]] = fds[1:]
    fds = input("Enter list of FDs seprated by space (-1 to end): ")

candidate_keys = input("Enter possible candidate key combinations(space seprated): ")
candidate_keys = candidate_keys.split()

if key_check(mega_relation, A, candidate_keys):
    print(f"{candidate_keys} CAN be the primary key")
else:
    print(f"{candidate_keys} CANNOT be the primary key")
