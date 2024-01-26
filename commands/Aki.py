def command(input_value, thread_userid=None):
    config = {
        "name": "Aki",
        "version": "1.0.0",
        "description": "Developer.",
        "credits": "𝑯𝒂𝒚𝒂𝒌𝒂𝒘𝒂 𝑨𝒌𝒊",
        "cooldown": "1"
    }
    if input_value == "__config__":
        return config
    elif input_value.startswith(config['name'] + ' ') or input_value == config['name']: 
    	return {'messages': ["DEVELOPED BY 𝑯𝒂𝒚𝒂𝒌𝒂𝒘𝒂 𝑨𝒌𝒊𝒊 Thanks For Using Ower Bot"], 'image': ['commands/images/onimai-oniichan-wa-oshimai.gif']}
    else:
        return {'messages': [f"Default option in {config['name']}: {config['description']}"]}
