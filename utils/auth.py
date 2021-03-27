import binascii
import hashlib
import os
import secrets


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwd_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                   salt, 100000)
    pwd_hash = binascii.hexlify(pwd_hash)
    return (salt + pwd_hash).decode('ascii')


def verify_password(stored_password, provided_password):
    # TODO: hash pwd on create and reimplement this
    # salt = stored_password[:64]
    # stored_password = stored_password[64:]
    # pwd_hash = hashlib.pbkdf2_hmac('sha512',
    #                                provided_password.encode('utf-8'),
    #                                salt.encode('ascii'),
    #                                100000)
    # pwd_hash = binascii.hexlify(pwd_hash).decode('ascii')
    # return secrets.compare_digest(pwd_hash, stored_password)
    return stored_password == provided_password
