tim_frontend = {"HTML", "CSS", "JavaScript", "React"} 
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}


print(tim_frontend.intersection(tim_backend))
print(tim_frontend & tim_backend)


print(tim_backend.difference(tim_frontend))
print(tim_backend - tim_frontend)


print(tim_frontend.intersection(tim_backend))
print(tim_frontend | tim_backend)