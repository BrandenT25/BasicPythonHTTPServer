resource "aws_security_group" "web_sg" {
    name = "http-server"
   
    ingress {
      from_port = 22
      to_port = 22
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
    
    ingress {
      from_port = 8000
      to_port = 8000
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]



    }
    egress{
    from_port = 0 
    to_port = 0 
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "web" { 
    ami = "ami-0a627a85fdcfabbaa"
    instance_type = "t3.micro"
    vpc_security_group_ids = [aws_security_group.web_sg.id]
    tags = {

    Name = "http-server"
  }
 }
