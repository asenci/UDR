class Udr < Formula
  desc "UDR is a wrapper around rsync that enables rsync to use UDT"
  homepage "https://github.com/LabAdvComp/UDR"
  url "https://github.com/asenci/UDR/archive/v0.9.4.tar.gz"
  version "0.9.4"
  revision 24
  sha256 "9e3f021f235ef6efa0a124f12f7e85c44969c26832914f299fe0441870c416ff"

  depends_on "openssl@1.1"
  depends_on "libudt"

  def install
    Dir.chdir('src')
    system "make -e os=OSX arch=AMD64"
    bin.install "udr"
  end
end
