Name:		texlive-wsuipa
Version:	25469
Release:	2
Summary:	International Phonetic Alphabet fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/wsuipa
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wsuipa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wsuipa.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a 7-bit IPA font, as Metafont source, and
macros for support under TeXt1 and LaTeX. The fonts (and
macros) are now largely superseded by the tipa fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/wsuipa/iaccent.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/igreekl.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/iparoman.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/iromanl.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/iromanp.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/iromanu.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wbxipa10.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wbxipa11.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wbxipa12.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wbxipa17.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wbxipa8.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wbxipa9.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wslipa10.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wslipa11.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wslipa12.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wslipa17.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wslipa8.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wslipa9.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wsuipa10.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wsuipa11.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wsuipa12.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wsuipa17.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wsuipa8.mf
%{_texmfdistdir}/fonts/source/public/wsuipa/wsuipa9.mf
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wbxipa10.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wbxipa11.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wbxipa12.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wbxipa17.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wbxipa8.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wbxipa9.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wslipa10.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wslipa11.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wslipa12.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wslipa17.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wslipa8.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wslipa9.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wsuipa10.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wsuipa11.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wsuipa12.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wsuipa17.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wsuipa8.tfm
%{_texmfdistdir}/fonts/tfm/public/wsuipa/wsuipa9.tfm
%{_texmfdistdir}/tex/latex/wsuipa/ipa.sty
%{_texmfdistdir}/tex/latex/wsuipa/ipalmacs.sty
%{_texmfdistdir}/tex/latex/wsuipa/uipa.fd
%doc %{_texmfdistdir}/doc/fonts/wsuipa/LICENCE-wsuipa.txt
%doc %{_texmfdistdir}/doc/fonts/wsuipa/README
%doc %{_texmfdistdir}/doc/fonts/wsuipa/changes.dec93
%doc %{_texmfdistdir}/doc/fonts/wsuipa/changes.jun91
%doc %{_texmfdistdir}/doc/fonts/wsuipa/changes.mar91
%doc %{_texmfdistdir}/doc/fonts/wsuipa/changes.may92
%doc %{_texmfdistdir}/doc/fonts/wsuipa/changes.nov90
%doc %{_texmfdistdir}/doc/fonts/wsuipa/compilefonts
%doc %{_texmfdistdir}/doc/fonts/wsuipa/ipamacs.tex
%doc %{_texmfdistdir}/doc/fonts/wsuipa/ipaman.ps
%doc %{_texmfdistdir}/doc/fonts/wsuipa/latex209/ipalman.tex
%doc %{_texmfdistdir}/doc/fonts/wsuipa/latex209/lipaman.tex
%doc %{_texmfdistdir}/doc/fonts/wsuipa/latex2e/ipaman.tex
%doc %{_texmfdistdir}/doc/fonts/wsuipa/text1/ipaman.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
