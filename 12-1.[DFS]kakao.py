def _create_query_dict(info):
    query_dict = {}
    '''
    query_dict: 
    {
        'javabackendjuniorpizza': '100', 
        'pythonfrontendseniorchicken': '200', 
        'cppseniorpizza': '250', 
        'backendsenior': '150', 
        'chicken': '100', 
        '': '150'
    }

    '''
    # {javabackendjuniorpizza:500,
    # cppseniorpizza:250..
    # }
    # ["java backend junior pizza 150",
    #  "python frontend senior chicken 210",
    for k in info:
        key = k[0]+k[1]+k[2]+k[3]
        key = key.replace('-', '')
        value = k[4]
        query_dict[key] = value

    print(f'query_dict: {query_dict}')
    return query_dict


def _split_queries(query):
    queries= []
    for q in query:
        q = q.split()  # q: ['java', 'and', 'backend', 'and', 'junior', 'and', 'pizza', '100']
        for i in range(3):
            q.remove('and')
        queries.append(q)
    print(queries)
    # queries:
    # [
    #   ['java', 'backend', 'junior', 'pizza', '100'],
    #   ['python', 'frontend', 'senior', 'chicken', '200'],
    #   ['cpp', '-', 'senior', 'pizza', '250'],
    #   ['-', 'backend', 'senior', '-', '150'],
    #   ['-', '-', '-', 'chicken', '100'],
    #   ['-', '-', '-', '-', '150']
    #   ]
    return queries


def _create_info_dict(info):
    '''
    info_dict:
        {'javabackendjuniorpizza': '150',
        'pythonfrontendseniorchicken': '150',
        'cppbackendseniorpizza': '260',
        'javabackendjuniorchicken': '80',
        'pythonbackendseniorchicken': '50'}
    '''
    info_dict = {}
    for i in info:
        i = i.split()
        key = i[0]+i[1]+i[2]+i[3]
        value = i[4]
        info_dict[key] = value

    return info_dict


def _find_if_contains_query(info_keys, query):
    for key in info_keys:
        if key.__contains__(query):
            return True
        else:
            return False


def solution(info, query):
    answer = []

    queries = _split_queries(query)
    query_dict = _create_query_dict(queries)
    info_dict = _create_info_dict(info)

    for query in query_dict:
        count = 0
        info_keys = info_dict.keys()

        if list(info_keys).__contains__(query):  # query 에 대해 부분 일치하는 key가 있는경우
            print(f'query: {query}')
            print(f'list_ info _keys: {list(info_keys)}')
            candidate_score = query_dict[query]
            standard_score = info_dict[query]

            if candidate_score >= standard_score:
                count += 1
        print(f'count: {query}: {count}')

        if not count == 0:
            answer.append(count)
        print(answer)
    return answer


def main():
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"
            ]
    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]

    solution(info, query)


if __name__ == "__main__":
    main()
