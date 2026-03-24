provider "aws" {
  region = "eu-north-1"
}

resource "aws_security_group" "ssh_access" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # SSH depuis n'importe où
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "master" {
  ami                    = "ami-0028b2c25f5ca28ed"
  instance_type          = "t3.micro"
  key_name               = "devops-key2"                    # <-- Nom exact de ta clé
  vpc_security_group_ids  = [aws_security_group.ssh_access.id]

  tags = {
    Name = "kubernetes-master"
  }
}

resource "aws_instance" "worker" {
  ami                    = "ami-0028b2c25f5ca28ed"
  instance_type          = "t3.micro"
  key_name               = "devops-key2"
  vpc_security_group_ids  = [aws_security_group.ssh_access.id]

  tags = {
    Name = "kubernetes-worker"
  }
}