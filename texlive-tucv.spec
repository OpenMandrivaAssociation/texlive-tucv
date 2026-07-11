%global tl_name tucv
%global tl_revision 20680

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Support for typesetting a CV or resumee
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tucv
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tucv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands for typesetting a CV or resume. It
provides commands for general-purpose headings, entries, and
item/description pairs, as well as more specific commands for formatting
sections, with explicit inclusion of school, degree, employer, job,
conference, and publications entries. It tends to produce a somewhat
long and quite detailed document but may also be suitable to support a
shorter resume. The package relies on a 'sufficiently recent' copy of
the l3kernel and l3packages bundles.

