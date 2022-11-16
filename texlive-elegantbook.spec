Name:		texlive-elegantbook
Version:	64122
Release:	1
Summary:	An Elegant LaTeX Template for Books
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elegantbook
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantbook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantbook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ElegantBook is designed for writing Books. This template is
based on the standard LaTeX book class. The goal of this
template is to make the writing process more elegant. Just
enjoy it!

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/elegantbook
%doc %{_texmfdistdir}/doc/latex/elegantbook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
