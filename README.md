## step 1 : we need to install the docker desktop

## step 2 : we need to crreate a dockerfile for guidelines
        **step 1 : we need to install the**
        - we will give the python image with version
        step 2 : install the python
        step 3 : install the packages
        - at a time or one by one
        step 4 : CMD python -m uvicorn --host --port --reload
        step 5 : last we will write how to run command

## step 3 : open docker desktop
         skip email
         if you get wsl error
         run below commands in CMD

         wsl --update
         wsl --set-default-version 2
         wsl --version

## step 4 : in your cmd first go to current working directory
         - docker build -t california-app .

         - it will run all the commands 

## step 5 : if image successfully available we can check

         in cmd type - docker images(we can see california app name)


