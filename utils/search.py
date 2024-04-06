def search(projects, entry):
    result = {}
    for project, attrib in projects.items():
        if project not in result:
            if project.lower().find(entry.lower()) != -1:
                print("matched")
                result[project] = attrib
            else:
                for key, value in attrib.items():
                    if value.lower().find(entry.lower()) != -1:
                        print("matched")
                        result[project] = attrib
    return result