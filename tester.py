import openai
import secret

openai.api_key=secret.api_key

sk=openai.Completion.create(
# CODIO SOLUTION BEGIN
    model="curie:ft-personal-2022-11-16-16-10-25",
    prompt="Codio sign: its tuesday ->"
# CODIO SOLUTION END    
    )

print(sk['choices'][0]['text'].strip())