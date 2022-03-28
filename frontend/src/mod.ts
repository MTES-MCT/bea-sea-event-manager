//https://github.com/denoland/deno/issues/12754#issuecomment-970386235
declare global {
  interface Crypto {
    randomUUID: () => string;
  }
}

console.log(crypto.randomUUID());

export {};
