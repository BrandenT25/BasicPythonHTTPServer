resource "aws_instance" "web" {
    ami = "ami-0a627a85fdcfabbaa"
    instance_type = "t3.micro"

    tags = {
        name = "http-server"
    }
}
