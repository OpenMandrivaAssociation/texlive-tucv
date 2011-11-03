# revision 20680
# category Package
# catalog-ctan /macros/latex/contrib/tucv
# catalog-date 2010-12-06 21:43:44 +0100
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-tucv
Version:	1.0
Release:	1
Summary:	Support for typesetting a CV or resumee
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tucv
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides commands for typesetting a CV or resume.
It provides commands for general-purpose headings, entries, and
item/description pairs, as well as more specific commands for
formatting sections, with explicit inclusion of school, degree,
employer, job, conference, and publications entries. It tends
to produce a somewhat long and quite detailed document but may
also be suitable to support a shorter resume.

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
%{_texmfdistdir}/tex/latex/tucv/tucv.sty
%doc %{_texmfdistdir}/doc/latex/tucv/README
%doc %{_texmfdistdir}/doc/latex/tucv/tucv.pdf
%doc %{_texmfdistdir}/doc/latex/tucv/tucv_ex.pdf
%doc %{_texmfdistdir}/doc/latex/tucv/tucv_ex.tex
#- source
%doc %{_texmfdistdir}/source/latex/tucv/tucv.dtx
%doc %{_texmfdistdir}/source/latex/tucv/tucv.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
