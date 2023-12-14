class Projects(object):
    def __init__(self, client):
        self._client = client

    def get_project(self, project_id, **kwargs):
        url = "projects/{}".format(project_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_projects(self, params=None, **kwargs):
        url = "projects"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def get_all_projects_with_filter(self, filter_id, params=None, **kwargs):
        url = "projects?filter_id={}".format(filter_id)
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_project(self, data, **kwargs):
        url = "projects"
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_project(self, project_id, data, **kwargs):
        url = "projects/{}".format(project_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_project(self, project_id, **kwargs):
        url = "projects/{}".format(project_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def duplicate_project(self, project_id, **kwargs):
        url = "projects/{}/duplicate".format(project_id)
        return self._client._post(self._client.BASE_URL + url, **kwargs)

    def get_project_details(self, project_id, **kwargs):
        url = "projects/{}".format(project_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def search_projects(self, params=None, **kwargs):
        url = "projects/search"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def get_project_plan(self, project_id, **kwargs):
        url = "projects/{}/plan".format(project_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_project_groups(self, project_id, **kwargs):
        url = "projects/{}/groups".format(project_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_project_tasks(self, project_id, **kwargs):
        url = "projects/{}/tasks".format(project_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_project_activities(self, project_id, **kwargs):
        url = "projects/{}/activities".format(project_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_project_fields(self, params=None, **kwargs):
        url = "projectFields"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def get_all_projects_boards(self, params=None, **kwargs):
        url = "projects/boards"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def get_board(self, board_id, **kwargs):
        url = "projects/boards/{}".format(board_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

