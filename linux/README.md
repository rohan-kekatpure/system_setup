# SSH setup

## Managing SSH keys

### Key generation

```
$ ssh-keygen -t rsa -C "<your_email@address.com>"
```

### Adding keys to agent

```bash
# Start the agent in the background
$ eval "$(ssh-agent -s)"

# List the keys in the agent
$ ssh-add -l

# Add a key in a file to the agent (conventionally in ~/.ssh)
$ ssh-add path/to/id_rsa

# Delete specific key
$ ssh-add -d /path/to/rd_rsa

# Clear out all keys in the agent
$ ssh-add -D
```
Further instructions can be found [here](http://stuff-things.net/2016/02/11/stupid-ssh-add-tricks/)

### Adding public keys to Github/Bitbucket

 1. Open repository settings

 2. Navigate to add/remove access keys 

     a. They are in different places in Github and Bitbucket. 

 3. Carefully copy-paste the key 

     a. (`pbcopy` command in MAC OS comes in handy)