move the `.service` file to `/lib/systemd/system/`

`sudo systemctl daemon-reload`
`sudo systemctl enable <.service file name>`
`sudo restart`

Copy the config file and update

`cp app/config.json.sample app/config.json`
`vim app/config.json`

