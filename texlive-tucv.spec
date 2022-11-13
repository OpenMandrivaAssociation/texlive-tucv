Name:		texlive-tucv
Version:	20680
Release:	1
Summary:	Support for typesetting a CV or resumee
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tucv
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands for typesetting a CV or resume.
It provides commands for general-purpose headings, entries, and
item/description pairs, as well as more specific commands for
formatting sections, with explicit inclusion of school, degree,
employer, job, conference, and publications entries. It tends
to produce a somewhat long and quite detailed document but may
also be suitable to support a shorter resume.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
