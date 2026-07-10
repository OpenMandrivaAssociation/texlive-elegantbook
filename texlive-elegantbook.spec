%global tl_name elegantbook
%global tl_revision 78872

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.7
Release:	%{tl_revision}.1
Summary:	An Elegant LaTeX Template for Books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/elegantbook
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantbook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantbook.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
ElegantBook is designed for writing Books. This template is based on the
standard LaTeX book class. The goal of this template is to make the
writing process more elegant.

