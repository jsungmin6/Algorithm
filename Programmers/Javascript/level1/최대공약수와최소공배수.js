function gcdlcm(a, b) {
  var gcd = calc_gcd(a, b);
  var lcm = (a * b) / gcd;

    return [gcd, lcm];
}

function calc_gcd(a, b) {
  if (b == 0) return a;
    return a > b ? calc_gcd(b, a % b) : calc_gcd(a, b % a);
}
