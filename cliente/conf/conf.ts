export class Conf{
  get(): {}{
    return {
      server: "http://localhost:10000/api/dev/",
    }
  }
}

export class Storage{
  add (key,value){
    localStorage.setItem(key, value);
  }

  load (key){
    return localStorage.getItem(key);
  }
}
