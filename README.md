# Rub-Hub

Simple console app where you can set up functionallity to be easily accessed.

Menus are created in json.

### Template
```
{
    "name": "name-of-menu",
    "options":[
        {
            "name": "option_1",
            "action": [
                {
                  <action>
                },
                {
                  <action>
                }
            ]
        },
        {
            "name": "option_2",
            "action": [
                {
                  <action>
                },
                {
                  <action>
                }
            ]
        }
    ]
}
```

### Actions
```
{
"LoadMenu": "<menu_name>.json" //program assumes this will be located in the local "Menus" folder
},
{
"OpenFile": "<path_to_file>"
},
{
"OpenFolder": "<path_to_folder>"
},
{
"RunPython": "<path_to_py_file>"
}
```


### Example
```
{
    "name": "Rub Stuff",
    "options":[
        {
            "name": "Open Rat Stuff",
            "action": [
                {
                "OpenFile": "C:/Users/ruby_/Desktop/python/ReallyFastRat/playerBigNew.png"
                },
                {
                "OpenFolder": "C:/Users/ruby_/Desktop/python/ReallyFastRat"
                }
            ]
        },
        {
            "name": "Run Test Program",
            "action": [
                {
                "RunPython": "RubHub/Programs/test.py"
                }
            ]
        },
        {
            "name": "Open Sub Menu",
            "action": [
                {
                "LoadMenu": "SubMenu.json"
                }
            ]
        }
    ]
}
```
