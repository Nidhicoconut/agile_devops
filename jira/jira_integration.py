import json
import os
from datetime import datetime

class MockJiraIntegration:
    """
    Mock Jira integration for demonstration purposes
    In a real environment, you would use the Jira API
    """
    def __init__(self, project_key="CALC"):
        self.project_key = project_key
        self.issues_file = "jira_issues.json"
        self.issues = self._load_issues()

    def _load_issues(self):
        if os.path.exists(self.issues_file):
            with open(self.issues_file, 'r') as f:
                return json.load(f)
        return []

    def _save_issues(self):
        with open(self.issues_file, 'w') as f:
            json.dump(self.issues, f, indent=2)

    def create_issue(self, summary, description, issue_type="Task"):
        """Create a new Jira issue"""
        issue_id = f"{self.project_key}-{len(self.issues) + 1}"
        new_issue = {
            "id": issue_id,
            "summary": summary,
            "description": description,
            "type": issue_type,
            "status": "To Do",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.issues.append(new_issue)
        self._save_issues()
        return issue_id

    def update_issue_status(self, issue_id, new_status):
        """Update an issue's status"""
        for issue in self.issues:
            if issue["id"] == issue_id:
                issue["status"] = new_status
                issue["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
        self._save_issues()

    def list_issues(self):
        """List all issues"""
        return self.issues


# Example usage
if __name__ == "__main__":
    jira = MockJiraIntegration()
    
    # Create a new feature issue
    feature_id = jira.create_issue(
        "Implement Power Function",
        "Add a new function to calculate power of numbers",
        "Feature"
    )
    print(f"Created feature: {feature_id}")
    
    # Create a task related to the feature
    task_id = jira.create_issue(
        "Write unit tests for Power Function",
        "Create comprehensive tests for the new power function",
        "Task"
    )
    print(f"Created task: {task_id}")
    
    # Update status after work is done
    jira.update_issue_status(feature_id, "Done")
    jira.update_issue_status(task_id, "Done")
    
    print("\nAll Jira Issues:")
    for issue in jira.list_issues():
        print(f"{issue['id']} - {issue['summary']} ({issue['status']})")
