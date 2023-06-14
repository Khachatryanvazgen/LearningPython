


class Profile:
    
    
    def __init__(self, first_name, last_name, profile_picture, cover_picture):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture
        
    def get_full_name(self):
        return self.first_name+' - '+self.last_name
        

user1 = Profile(first_name = 'Vazgen', last_name = 'Khachatryan',profile_picture = 'vk.jpeg',cover_picture = 'vk_cover.jpeg' )


print(user1.get_full_name())
# print(user1.last_name)