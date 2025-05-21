# Update Submodule GitHub Template Repository
A repository containing a GitHub workflow to update submodules and optionally be used as a template repository

This repository can be used either as a template or as a resource from which to copy the workflow.

## Workflow usage:
1. Copy the `.github/` directory found [HERE](https://github.com/JackEAllen/Update_Submodule_Action_Template/tree/main/.github/workflows) which contains [THIS](https://github.com/JackEAllen/Update_Submodule_Action_Template/blob/main/.github/workflows/update_submodule.yml) `.yml` file containing the GitHub workflow to the root of the submodule repository that you would like to be update automatically in the subsequent parent repository.

2. Modify the [update_submodule.yml](https://github.com/JackEAllen/Update_Submodule_Action_Template/blob/main/.github/workflows/update_submodule.yml) script, changing the `PARENT_REPO_BRANCH` variable to the name of your parent branch if not "main" by default on the parent repository and also change the branch name on line 5 if not wishing to update on changes to main in the child repo.
If you change the branch name on line 5 to a sub-branch off the main branch, you will also need to modify line 29 of the workflow, replacing it with the following statement: `git switch -c ${{ github.ref_name }} remotes/origin/${{ github.ref_name }}`

3. Create a personal access token for your the github organization that you would like to update the submodule in. Please [SEE HERE](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for more details on how to do this. The token will need the following permissions:
    - repo
    - workflow

4. Save the token as a repository secret in the child repository and parent repository under name `PRIVATE_TOKEN_GITHUB`. [SEE HERE](https://docs.github.com/en/actions/security-guides/encrypted-secrets) for more details on how to do this.

5. Create a new branch in the child repository and make a change to the README.md file. Commit the change and push the branch to the remote repository. You should see the workflow run and update the submodule in the parent repository. To verify this, you can check the status of the workflow in the actions tab of the child repository and also check the submodule in the parent repository to see if it has been updated. 

---

### Things to Note:

**Using this workflow in a GitHub organisation using a regular GitHub user personal access token should be avoided**

For use with an organization, you will need to create a personal access token for the organization and save it as a repository secret in both the child and parent repositories. The token will need the following permissions:

* repo
* workflow

Otherwise, I suggest one of the two other possible integrations:
1. Convert this workflow to a GitHub app and use the app to update the submodule. This will allow you to use a GitHub app token instead of a personal access token. [SEE HERE](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps) for more details on GitHub apps.
2. Adapt this workflow to be used by an alternative CI/CD tool such as [Jenkins](https://www.jenkins.io/doc/tutorials/) or [Travis CI](https://docs.travis-ci.com/user/tutorial/). This should be relatively straight forward as both tools can be used using yaml similarly to GitHub actions.

---

### Useful Information
To toggle enabling and disabling a workflow once added to a repository using GitHub actions, please see [HERE](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow)
