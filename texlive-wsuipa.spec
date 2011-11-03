# revision 15878
# category Package
# catalog-ctan /fonts/wsuipa
# catalog-date 2008-12-04 21:34:53 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-wsuipa
Version:	20081204
Release:	1
Summary:	International Phonetic Alphabet fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/wsuipa
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wsuipa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wsuipa.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a 7-bit IPA font, as MetaFont source, and
macros for support under TeXt1 and LaTeX. The fonts (and
macros) are now largely superseded by the tipa fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_texmfdistdir}/doc/generic/wsuipa/LICENCE-wsuipa.txt
%doc %{_texmfdistdir}/doc/generic/wsuipa/README
%doc %{_texmfdistdir}/doc/generic/wsuipa/changes.dec93
%doc %{_texmfdistdir}/doc/generic/wsuipa/changes.jun91
%doc %{_texmfdistdir}/doc/generic/wsuipa/changes.mar91
%doc %{_texmfdistdir}/doc/generic/wsuipa/changes.may92
%doc %{_texmfdistdir}/doc/generic/wsuipa/changes.nov90
%doc %{_texmfdistdir}/doc/generic/wsuipa/compilefonts
%doc %{_texmfdistdir}/doc/generic/wsuipa/ipamacs.tex
%doc %{_texmfdistdir}/doc/generic/wsuipa/ipaman.ps
%doc %{_texmfdistdir}/doc/generic/wsuipa/latex209/ipalman.tex
%doc %{_texmfdistdir}/doc/generic/wsuipa/latex209/lipaman.tex
%doc %{_texmfdistdir}/doc/generic/wsuipa/latex2e/ipaman.tex
%doc %{_texmfdistdir}/doc/generic/wsuipa/text1/ipaman.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
