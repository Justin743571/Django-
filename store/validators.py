from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_kb = 50
    
    if file.size > max_size_kb * 1024 :
        raise ValidationError('文件不能高于50kb')
        