# Agent Instructions for WebsiteWTCjeugd

## Git Version Control

**All git operations (commit, push, pull, branch management) are handled by the user.**

Do not perform any git commands (git add, git commit, git push, git pull, git checkout, git branch, etc.) unless explicitly requested by the user in the current conversation turn. This includes:
- Creating new branches
- Committing changes
- Pushing to remote repositories
- Merging branches
- Any other git operations

The user will handle all version control manually. Focus on creating, editing, and saving files in the repository as requested.

## File Creation and Editing

- Create and edit files in the repository as requested
- Save files to the correct locations (e.g., `websiteteksten/` for website texts)
- Use the existing structure from `Websitestructuur-jeugd.md` as the source of truth
- Follow the naming conventions specified in the structure document
- **When creating new website text files, always update `Websitestructuur-jeugd.md` to include the new file in the appropriate table**
- **When creating new naslag files, also update the index page `07-naslag-voor-leden.md` with a link to the new page**

## General

- Follow the jeugdsport-teksten skill for WTC Woerden content
- Use Dutch language for all content
- Maintain the tone and style appropriate for the target audience (jeugd/ouders)
- When in doubt about facts (dates, times, locations, costs), ask the user for verification