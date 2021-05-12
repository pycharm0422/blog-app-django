from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image

class Posts(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = RichTextField(null=True, blank=True)
    public_view = models.BooleanField(default=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    def get_likes_count(self):
        return self.likes.count()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}  Profile" 

    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)
 
    #     if img.height > 400 or img.height < 400 or img.width > 400 or img.width < 400:
    #         output_size = (400, 400)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=True)

    def __str__(self):
        return f"{self.user} Comment"






# <script type="text/javascript" >

# //     $(document).ready(function(event){
# //         $(document).on('click', '#like', function(event){
# //             event.preventDefault();
# //             var pk = $(this).attr('value');
# //             $.ajax({
# //                 type: 'POST',
# //                 url: '{% url "liked-post" %}',
# //                 data: {'post_id':pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
# //                 dataType: 'json',
# //                 success: function(response){
# //                     $('#like-section').html(response['form'])
# //                     console.log($('#like-section').html(response['form']));
# //                 },
# //                 error: function(rs, e){
# //                     console.log(rs.responseText);
# //                 },

# //             });
# //         });
# //     });

# // </script>
# <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
# <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script> -->
# <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
