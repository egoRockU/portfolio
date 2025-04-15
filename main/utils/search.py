def search(projects, entry):
    result = {}
    for project, attrib in projects.items():
        if project not in result:
            if project.lower().find(entry.lower()) != -1:
                result[project] = attrib
            else:
                for key, value in attrib.items():
                    if isinstance(value, str):
                        if value.lower().find(entry.lower()) != -1:
                            result[project] = attrib
                    elif isinstance(value, list):
                        for item in value:
                            if item.lower().find(entry.lower()) != -1:
                                result[project] = attrib
    return result