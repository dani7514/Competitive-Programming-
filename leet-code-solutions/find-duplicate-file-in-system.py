class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)

        for path_info in paths:
            path_elements = path_info.split()
            directory = path_elements[0]
            files = path_elements[1:]

            for file_info in files:
                file_start = file_info.index('(')
                file_name = file_info[:file_start]
                file_content = file_info[file_start + 1:-1]

                full_path = directory + '/' + file_name
                content_to_paths[file_content].append(full_path)

        duplicates = [group for group in content_to_paths.values() if len(group) > 1]
        return duplicates
