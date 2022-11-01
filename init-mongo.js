db.createUser({
    user: 'admin',
    password: 'mongoadmin',
    roles:[
      {
        role: 'readWrite',
        db: 'admin',
      },
    ],
  });